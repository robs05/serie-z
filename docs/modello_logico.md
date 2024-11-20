tornei(ID_torneo PK, nome, descrizione, data_inizio, data_fine)

tornei_squadre(ID, id_torneo FK, id_squadra FK)

squadre(ID_squadra PK, nome, num_max_giocatori, colore_divisa)

classifiche(ID, id_squadra FK, id_classifica, punti, pv, pn, pp, gf, gs, dr)

partecipanti(ID_partecipante, nome, cognome, data_nascita, ruolo, capitano, num_maglia, id_squadra FK)

partite(ID_partita, data_ora, id_squadra_a FK, id_squadra_b FK, goal_a, goal_b)

arbitri(ID_arbitro, nome, cognome, data_nascita, anni_esperienza)
