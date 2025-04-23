import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Calculadora"
    pagina.bgcolor = "#2d2d2d"
    pagina.window.width = 350
    pagina.window.height = 470


    todos_valores = ""
    
    resultado_texto = ft.Text(value="0", size=29, color="white", text_align="right")

    def entrar_valores(e):
        nonlocal todos_valores
        todos_valores += str(e.control.text)
        resultado_texto.value = todos_valores
        pagina.update()
        
    def limpar_tela(e):
        nonlocal todos_valores
        todos_valores = ""
        resultado_texto.value = 0
        pagina.update()
        
    def backspace(e):
        nonlocal todos_valores
        todos_valores = todos_valores[:-1]
        resultado_texto.value = todos_valores if todos_valores else '0'
        pagina.update()
        
    def calcular(e):
        nonlocal todos_valores
        try:
            resultado_texto.value = str(eval(todos_valores))
            todos_valores = resultado_texto.value
        except:
            resultado_texto.value = "error"
            todos_valores = ""
        pagina.update()

    tela = ft.Container(
        content=resultado_texto,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right
    )

    # estilização dos botões
    estilo_numeros = {
        "height": 60,
        "bgcolor": "#4d4d4d",
        "color": "white",
        "expand": 1,
    }
    
    estilo_operadores = {
        "height": 60,
        "bgcolor": "#FF370",
        "color": "white",
        "expand": 1,
    }
    estilo_limpar = {
        "height": 60,
        "bgcolor": "#FF3B30",
        "color": "white",
        "expand": 1,
    }
      
    estilo_igual = {
        "height": 60,
        "bgcolor": "#34C759",
        "color": "white",
        "expand": 1,
    }

    grade_botoes = [
        [("C", estilo_limpar,limpar_tela),("%", estilo_operadores,entrar_valores), ("/", estilo_operadores,entrar_valores), ("*", estilo_operadores,entrar_valores)],
        [("7",estilo_numeros,entrar_valores), ("8",estilo_numeros,entrar_valores), ("9",estilo_numeros,entrar_valores),   ("-",estilo_operadores,entrar_valores),],
        [("4",estilo_numeros,entrar_valores), ("5",estilo_numeros,entrar_valores), ("6",estilo_numeros,entrar_valores), ("+",estilo_operadores,entrar_valores),],
        [("1",estilo_numeros), ("2",estilo_numeros), ("3",estilo_numeros), ("⌫",estilo_limpar,backspace),],
        [("0", {**estilo_numeros, "expand": 2},entrar_valores), (".",estilo_numeros,entrar_valores), ("=",estilo_igual,calcular)],
    ]

    botoes = []
    for linha in grade_botoes:
        linha_control = []
        for item in linha:
            if len(item) == 3:
                texto, estilo, handler = item
                btn = ft.ElevatedButton(
                    text=texto,
                    on_click=handler,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        padding=5
                    ),
                    **estilo
                )
            else:
                texto, estilo = item
                btn = ft.ElevatedButton(
                    text=texto,
                    on_click=entrar_valores,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        padding=5
                    ),
                    **estilo
                )
            linha_control.append(btn)
        botoes.append(ft.Row(linha_control, spacing=5))

    pagina.add(
        ft.Column(
            [
                tela,
                ft.Column(botoes, spacing=5)
            ]
        )
    )

ft.app(target=main)