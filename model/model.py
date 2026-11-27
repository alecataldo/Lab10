import networkx as nx
from database.dao import DAO
from model.bonifico import Bonifico


class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO
        #Recupero filiali e bonifici
        self._nodes = DAO.get_all_filiali()
        self._edges = DAO.read_all_bonifici()

        #Svuoto il grafo
        self.G.clear()

        #Aggiungo le filiali come nodi
        for filiale in self._nodes.values():
            self.G.add_node(filiale)

        #Trovo i collegamenti tra filiali
        collegamenti = {}

        for bonifico in self._edges.values():
            coppia = tuple(sorted(
                (bonifico.id_filiale_origine, bonifico.id_filiale_destinazione)))

            if coppia not in collegamenti:
                collegamenti[coppia] = []

            collegamenti[coppia].append(bonifico.importo)

        #Calcolo le medi e inserisco gli archi
        for coppia,importi in collegamenti.items():
            media = sum(importi) / len(importi)

            if media > threshold:
                id1, id2 = coppia
                self.G.add_edge(self._nodes[id1], self._nodes[id2], weight = media)






    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        #Networkx ha una funzione per farlo
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        #Networkx ha una funzione per farlo
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        #Networkx ha una funzione per farlo
        return self.G.edges(data=True)
