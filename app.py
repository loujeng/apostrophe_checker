import gradio as gr
from checker import ApostropheChecker

checker = ApostropheChecker()


def check_text(text):
    try:
        highlighted = checker.highlight_errors(text)
        corrected = checker.correct_text(text)
        return highlighted, corrected, ""
    except ValueError as e:
        return "", "", str(e)


with gr.Blocks() as demo:
    gr.Markdown("## Перевірка апострофа")
    gr.Markdown(
        "Введіть текст нижче, щоб перевірити правильність вживання апострофа. "
        "Помилки буде виділено червоним кольором, а виправлений текст відображатиметься окремо."
    )

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="Введіть текст",
                placeholder="Наприклад: Лукяна, п’ять, міжярусний"
            )
        with gr.Column():
            highlighted_output = gr.HTML(label="Текст із помилками")
            corrected_output = gr.Textbox(label="Виправлений текст")

    error_output = gr.Textbox(label="Повідомлення про помилку", interactive=False)
    submit_btn = gr.Button("Перевірити")

    submit_btn.click(
        fn=check_text,
        inputs=input_text,
        outputs=[highlighted_output, corrected_output, error_output]
    )

demo.launch()
