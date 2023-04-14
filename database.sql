// Use DBML to define your database structure
// Docs: https://www.dbml.org/docs

Table celular {
  numero_de_serie integer [primary key]
  marca text
  modelo text
  preco integer 
}

Table clientes {
  cpf integer [primary key]
  nome text
  endereco text
  celular integer
}

Table endereco {
  PK integer [primary key]
  Rua text
  numero integer
  CEP integer
  complemento text
}


Ref: "clientes"."endereco" < "endereco"."PK"

Ref: "clientes"."celular" < "celular"."numero_de_serie"