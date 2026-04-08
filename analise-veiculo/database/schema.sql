CREATE TABLE vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_veiculo INTEGER,
    data_venda TEXT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    FOREIGN KEY (id_veiculo) REFERENCES veiculos(id)
);

-- criar tabelas via SQL