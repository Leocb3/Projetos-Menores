<p align="center"><img src="https://vignette.wikia.nocookie.net/megaman/images/2/22/Cutman.png"></p>
<h2 align="center"><b>MegaMan API</b></h2>
<p align="center">
<a href="https://dotnet.microsoft.com/" alt="Dotnet"><img src="https://img.shields.io/badge/dotnet-3.1-%235c2d91.svg"></a>
<a href="https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/3.1.8" alt="EF Core"><img src="https://img.shields.io/badge/EntityFrameworkCore-3.1.8-%235c913b.svg"></a>
<a href="https://www.nuget.org/packages/Newtonsoft.Json/12.0.2" alt="Newtonsoft Json"><img src="https://img.shields.io/badge/Newtonsoft.Json-12.0.2-%23ff554d.svg"></a>
</p>
<p align="center">Backend para listar dados dos bosses de MegaMan</p>
<hr>

## Exemplo de Resposta JSON

```json
{
  "Id": 1,
  "Code": "DLN/DRN-003",
  "Name": "Cutman",
  "HP": 150,
  "Picture": "https://vignette.wikia.nocookie.net/megaman/images/2/22/Cutman.png"
}
```

## Endpoints da API

- **GET `api/v1/robots`**: Lista todos os robôs.
- **GET `api/v1/robots/{id}`**: Retorna detalhes de um robô pelo ID.
- **POST `api/v1/robots`**: Adiciona um novo robô.

## Estrutura do Projeto

```plaintext
.vs
.vscode
bin
Controllers
Database
middlewares
Models
obj
Properties
Services
appsettings.Development.json
appsettings.json  
global.json
MegamanApi.csproj  
MegamanApi.sln
Program.cs
Startup.cs
```

## Dependências

| Dependência | Versão | Descrição |
| ----------- | -------| --------- |
| [Microsoft.EntityFrameworkCore](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore/3.1.8) | 3.1.8 | Framework ORM para .NET Core. |
| [Microsoft.EntityFrameworkCore.Design](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.Design/3.1.8) | 3.1.8 | Ferramentas de design para Entity Framework Core. |
| [Microsoft.EntityFrameworkCore.SqlServer](https://www.nuget.org/packages/Microsoft.EntityFrameworkCore.SqlServer/3.1.8) | 3.1.8 | Provedor de banco de dados SQL Server para Entity Framework Core. |
| [Newtonsoft.Json](https://www.nuget.org/packages/Newtonsoft.Json/12.0.2) | 12.0.2 | Biblioteca para serialização e desserialização de JSON em .NET. |

## Técnicas Utilizadas

### **Controllers**
Os controllers são responsáveis por gerenciar os endpoints da API e encaminhar as requisições aos serviços apropriados.

### **Database**
A pasta Database contém as migrações e o contexto do Entity Framework Core, facilitando a comunicação com o banco de dados.

### **Middlewares**
A pasta middlewares armazena middlewares personalizados que tratam requisições e respostas, adicionando camadas de lógica adicional.

### **Models**
Contém classes de modelos de dados que representam as entidades da aplicação.

### **Services**
Serviços contêm a lógica de negócio e comunicação com a camada de dados.

## Configurações
As configurações do projeto são gerenciadas pelos arquivos `appsettings.Development.json` e `appsettings.json`, permitindo a personalização do ambiente de execução.

## Inicialização
Os arquivos `Program.cs` e `Startup.cs` contêm a configuração e inicialização da aplicação, incluindo a injeção de dependências e configuração do pipeline de requisições.

```
# Arquitetura
src
    📂|- Controllers
    📂|- Services
    📂|- Database
        📂|- DTOs
        📂|- EntityFramework
        📂|- Repositories
    📂|- Middlewares
    📂|- Models
``` 

Para mais detalhes sobre o projeto, consulte os arquivos e diretórios acima mencionados.

🤓 Leonardo Chung Bezerra -
[GitHub](https://github.com/Leocb3)
