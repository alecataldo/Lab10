import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO
        try:
            threshold = float(self._view.importo_medio_minimo.value)
        except ValueError:
            self._view.show_alert("Inserisci un importo numerico valido!")
            return

        #Costruisco il grafo
        self._model.costruisci_grafo(threshold)

        # Recupero il numero di filiali e collegamenti
        num_nodi = self._model.get_num_nodes()
        num_archi = self._model.get_num_edges()

        # Recupero tutti i collegamenti
        archi = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di filiali: {num_nodi}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di collegamenti: {num_archi}"))
        self._view.update()

        # Visualizzo tutti i collegamenti
        for filiale1, filiale2, dati in archi:
            peso = dati["weight"]

            self._view.lista_visualizzazione.controls.append(
                ft.Text(
                    f"{filiale1} <-> {filiale2}: {peso:.2f} €"
                )
            )

        self._view.update()

