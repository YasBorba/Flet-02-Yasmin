import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = "#f3f0f9"

    texto_cor = "#6a1b9a"
    texto_claro = "#e0e0e0"

    # Atualizar cores
    def atualizar_cores():
        titulo.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        subtitulo.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        resultado.color = texto_claro if page.theme_mode == ft.ThemeMode.DARK else texto_cor
        page.update()

    # Alternar tema
    def toggle_tema(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = "#1f1b2e"
            tema_btn.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = "#f3f0f9"
            tema_btn.icon = ft.Icons.DARK_MODE
        atualizar_cores()

    # Campos
    nome = ft.TextField(
        label="Nome",
        width=300,
        prefix_icon=ft.Icons.PERSON,
        border_color="#6a1b9a"
    )
    peso = ft.TextField(
        label="Peso (kg)",
        width=300,
        prefix_icon=ft.Icons.FITNESS_CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color="#6a1b9a",
    )
    altura = ft.TextField(
        label="Altura (m)",
        width=300,
        prefix_icon=ft.Icons.HEIGHT,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_color="#6a1b9a",
    )

    resultado = ft.Text(
        size=20,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        color=texto_cor,
    )

    # Conatainer para os cards de resultado
    cards_container = ft.Column(
        width=350,
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Função para criar e adicionar um card de resultado
    def criar_card_resultado(nome_valor, peso_valor, altura_valor, imc_valor, classificacao_valor):
        novo_card = ft.Card(
            elevation=4,
            content=ft.Container(
                content=ft.Column(
                    [
                       ft.Text(nome_valor, size=18, weight=ft.FontWeight.BOLD, color="#6a1b9a"),
                       ft.Text(f"Peso: {peso_valor} kg", size=14),
                       ft.Text(f"Altura: {altura_valor} m", size=14),
                       ft.Text(f"IMC: {imc_valor:.2f}", size=16, weight=ft.FontWeight.BOLD),
                       ft.Text(f"Classificação: {classificacao_valor}", size=16, color=ft.Colors.RED_900 if 'Obesidade' in classificacao_valor else ft.Colors.GREEN_800)  
                    ]
                ),
                padding=20,
            ),
            width=300,
            margin=ft.margin.symmetric(vertical=10),
        )
        cards_container.controls.append(novo_card)
        page.update()

    # Calcular IMC
    def calcular_imc(e):
        try:
            p = float(peso.value.replace(",", "."))
            a = float(altura.value.replace(",", "."))
            n = nome.value.strip()
            if p <= 0 or a <= 0:
                resultado.value = "⚠️ Informe valores válidos!"
            else:
                imc = p / (a * a)
                if imc < 18.5:
                    classificacao = "Abaixo do peso"
                elif imc < 24.9:
                    classificacao = "Peso normal"
                elif imc < 29.9:
                    classificacao = "Sobrepeso"
                elif imc < 34.9:
                    classificacao = "Obesidade grau I"
                elif imc < 39.9:
                    classificacao = "Obesidade grau II"
                else:
                    classificacao = "Obesidade grau III"
                
                # Cria e adiciona o card de resultado
                criar_card_resultado(n, p, a, imc, classificacao)
                # Exibe o resultado temporariamente no campo de texto
                resultado.value = f"📊 IMC calculado e salva"
        except:
            resultado.value = "⚠️ Preencha peso e altura corretamente!"
        page.update()

    # Limpar campos
    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = ""
        page.update()

    # Botão de alternância de tema
    tema_btn = ft.IconButton(
        ft.Icons.DARK_MODE,
        on_click=toggle_tema,
        icon_color="#c569fe",
    )

    # Botão calcular
    btn_calcular = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Text("Calcular IMC", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        bgcolor="#6a1b9a",
        width=180,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        on_click=calcular_imc,
    )

    # Botão limpar com ícone
    btn_limpar = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Image(src="icon.png", width=24, height=24),
                ft.Text("Limpar", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        bgcolor="#d32f2f",
        width=150,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
        on_click=limpar,
    )

    # Textos principais
    titulo = ft.Text(
        "Calculadora de IMC",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=texto_cor,
        text_align=ft.TextAlign.CENTER,
    )
    subtitulo = ft.Text(
        "Informe seus dados",
        size=16,
        color=texto_cor,
        text_align=ft.TextAlign.CENTER,
    )

    # Layout
    page.add(
        ft.Column(
            [
                ft.Image(src="Senai.png", width=150, height=80),
                ft.Row([titulo, tema_btn], alignment=ft.MainAxisAlignment.CENTER),
                subtitulo,
                nome,
                peso,
                altura,
                ft.Row(
                    [btn_calcular, btn_limpar],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                resultado,
                resultado,
                ft.Divider(height=10, color="transparent"),
                ft.Text("Resultados Salvos", size=16, weight=ft.FontWeight.BOLD, color=texto_cor),
                ft.Divider(height=2, color="#6a1b9a"),
                cards_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

ft.app(target=main)
