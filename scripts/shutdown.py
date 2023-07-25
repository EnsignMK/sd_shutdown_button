from modules import shared, script_callbacks
from modules import script_callbacks
import gradio as gr
import os






js = """function close_window() {
  if (confirm("Close the application?")) {
    return true;
  } else {
    return false;
  }
}
"""

def stop_button(component, **kwargs):
    after_this_compo = "setting_{}".format(shared.opts.data["quicksettings_list"][-1])

    # print(after_this_compo)

    if kwargs.get("elem_id") == after_this_compo:
        with gr.Row(elem_id="quicksettings", variant="compact"):
            btn = gr.Button("Exit ⭕", elem_id="stop_button",size="sm",variant='stop')
            hidden_checkbox = gr.Checkbox(visible=False)

            def when(hidden_state):
                if hidden_state:
                    os._exit(0)
                return False

            btn.click(when, hidden_checkbox, hidden_checkbox, _js=js)




script_callbacks.on_after_component(stop_button)
