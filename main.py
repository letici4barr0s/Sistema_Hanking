import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from database import criar_tabela, buscar_listas, buscar_por_lista
from utils import importar_csv

class RankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Sistema de Ranking de Jogadores")
        self.root.geometry("750x500")
        self.root.resizable(False, False)

        # Título
        titulo = ttk.Label(root, text="🏆 Ranking de Jogadores", font=("Segoe UI", 16, "bold"))
        titulo.pack(pady=10)

        # Frame principal dividido
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="both", expand=True)

        # Menu lateral
        menu_frame = ttk.Frame(frame)
        menu_frame.pack(side="left", fill="y", padx=10)

        btn_importar = ttk.Button(menu_frame, text="📂 Importar CSV", width=20, command=self.importar_csv)
        btn_importar.pack(pady=10)

        btn_listas = ttk.Button(menu_frame, text="📊 Exibir Ranking", width=20, command=self.exibir_listas)
        btn_listas.pack(pady=10)

        btn_sair = ttk.Button(menu_frame, text="❌ Sair", width=20, command=root.quit)
        btn_sair.pack(pady=10)

        # Área de exibição com Data Grid (Treeview)
        display_frame = ttk.Frame(frame)
        display_frame.pack(side="right", fill="both", expand=True)

        colunas = ("Posição", "Nome", "Nível", "Pontuação")
        self.tree = ttk.Treeview(display_frame, columns=colunas, show="headings", height=20)

        # Cabeçalhos
        self.tree.heading("Posição", text="Posição")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Nível", text="Nível")
        self.tree.heading("Pontuação", text="Pontuação")

        # Ajustando largura
        self.tree.column("Posição", width=80, anchor="center")
        self.tree.column("Nome", width=200, anchor="w")
        self.tree.column("Nível", width=80, anchor="center")
        self.tree.column("Pontuação", width=100, anchor="center")

        # Scrollbars
        scrollbar_y = ttk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscroll=scrollbar_y.set)

        scrollbar_x = ttk.Scrollbar(display_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscroll=scrollbar_x.set)

        self.tree.pack(fill="both", expand=True)

    def importar_csv(self):
        arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo CSV",
            filetypes=[("CSV files", "*.csv")]
        )
        if arquivo:
            try:
                lista_id = len(buscar_listas()) + 1
                importar_csv(arquivo, lista_id)
                messagebox.showinfo("Sucesso", f"✅ Dados importados para a lista {lista_id}!")
            except Exception as e:
                messagebox.showerror("Erro", f"❌ Falha ao importar CSV:\n{e}")

    def exibir_listas(self):
        listas = buscar_listas()
        if not listas:
            messagebox.showwarning("Aviso", "Nenhuma lista encontrada!")
            return

        # Janela para escolher lista
        lista_win = tk.Toplevel(self.root)
        lista_win.title("Escolher Lista de Ranking")
        lista_win.geometry("300x150")
        lista_win.resizable(False, False)

        ttk.Label(lista_win, text="Selecione uma lista:", font=("Segoe UI", 11)).pack(pady=10)

        combo = ttk.Combobox(lista_win, values=listas, state="readonly")
        combo.pack(pady=5)
        combo.current(0)

        def mostrar_ranking():
            lista_id = combo.get()
            jogadores = buscar_por_lista(lista_id)
            if jogadores:
                self.mostrar_ranking(jogadores, lista_id)
            else:
                messagebox.showinfo("Info", "Nenhum jogador nessa lista.")
            lista_win.destroy()

        ttk.Button(lista_win, text="Mostrar", command=mostrar_ranking).pack(pady=10)

    def mostrar_ranking(self, jogadores, lista_id):
        # Limpar tabela
        for row in self.tree.get_children():
            self.tree.delete(row)

        for i, (nome, nivel, pontuacao) in enumerate(jogadores, start=1):
            if i == 1:
                destaque = "🥇"
            elif i == 2:
                destaque = "🥈"
            elif i == 3:
                destaque = "🥉"
            else:
                destaque = str(i)
            self.tree.insert("", tk.END, values=(destaque, nome, nivel, pontuacao))

if __name__ == "__main__":
    criar_tabela()
    root = tk.Tk()
    app = RankingApp(root)
    root.mainloop()
