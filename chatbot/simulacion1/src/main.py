import flet as ft

def main(page: ft.Page):
    page.title = "🤖Chatbot - Parte 1"
    page.bgcolor = ft.Colors.BLUE_200

    mensajes = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
    prompt = ft.TextField(
        label="Escribe tu mensaje...", expand=True,
        multiline=False,
        min_lines=1,
        max_lines=4
    )

    def burbuja(texto, chatsito):
        return ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        texto,
                        color=ft.Colors.BLACK87,
                        size=15,
                        selectable=True,
                    ),
                    bgcolor=ft.Colors.BLUE_50 if chatsito else ft.Colors.CYAN_50,
                    padding=12,
                    border_radius=30,
                    width=350,
                )
            ],
            alignment=ft.MainAxisAlignment.END if chatsito else ft.MainAxisAlignment.START,
        )

    def enviar_click(e):
        texto = prompt.value.strip()
        if not texto:
            return
        mensajes.controls.append(burbuja(texto, chatsito=True))
        prompt.value = ""
        page.update()
        mensajes.controls.append(burbuja("Hola, soy una simulación👋", chatsito=False))
        page.update()

    def limpiar_chat(e):
        mensajes.controls.clear()
        page.update()

    boton_enviar = ft.ElevatedButton(
        "Enviar",
        on_click=enviar_click,
        bgcolor=ft.Colors.CYAN_ACCENT,
        color=ft.Colors.BLACK87
    )

    boton_limpiar = ft.TextButton("🧹Limpiar chat", on_click=limpiar_chat, style=ft.ButtonStyle(color=ft.Colors.BLUE_900))
    prompt.on_submit = enviar_click

    page.add(
        ft.Column(
            [
                ft.Row(
                    [ft.Text("🤖Chatbot - Parte 1", size=18, color=ft.Colors.BLACK), boton_limpiar],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                mensajes,
                ft.Row([prompt, boton_enviar], vertical_alignment=ft.CrossAxisAlignment.END),
            ],
            expand=True
        )
    )


ft.app(target=main)