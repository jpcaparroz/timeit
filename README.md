# timeit
TimeiT

---

## 🔩 Requirements

- Python

<br> 

## 🟢 Initiate
To start using or developing, install the necessary libraries using the commands:


* Create venv
  #####
      python -m venv .venv

* Install libs
  #####
      pip install -r .\requirements.txt

* Initialize venv
  #####
      .\.venv\Scripts\activate


<br> 

## ♨️ Notion Infos

To get notion database id, follow below image:

[database-id](./docs/images/notion-database-id-tutorial.png)


<br> 

## ⚙️ Env Parameters

To initiate, the archive `.env` must be fill, like below:

[.env](/.env)
#####
    NOTION_API_TOKEN= secret_CpVDPSMKKioeioiojmz                                   # [string] Notion Service User API Token
    NOTION_DATABASE_TIMEIT_ID= 07c7e9ce34r5fsdf443                                 # [string] Notion timeit Database ID
    NOTION_DATABASE_TIMEIT_HISTORICAL_ID= 07c7e9cdzcxfr345dde7c188fa9c3            # [string] Notion timeit-historical Database ID
    NOTION_DATE_FORMAT_TIMEIT= %Y-%m-%d                                            # [string] Python datetime format https://docs.python.org/pt-br/3.10/library/datetime.html#strftime-and-strptime-format-codes
    NOTION_DATE_FORMAT_TIMEIT_HISTORICAL= %Y-%m-%d                                 # [string] Python datetime format https://docs.python.org/pt-br/3.10/library/datetime.html#strftime-and-strptime-format-codes

##### Copy below to make your .env file =)
    NOTION_API_TOKEN= 
    NOTION_DATABASE_TIMEIT_ID=
    NOTION_DATABASE_TIMEIT_HISTORICAL_ID=
    NOTION_DATE_FORMAT_TIMEIT=
    NOTION_DATE_FORMAT_TIMEIT_HISTORICAL=

<br> 

## ⚠️ Important

- Make sure all dependencies are installed correctly.

<br> 

## 🤝 Colaborators

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/jo%C3%A3o-pedro-dias-caparroz-2b19a1161/" title="Linkedin Profile Icon">
        <img src="https://media.licdn.com/dms/image/C4D03AQHVyVT6CT6TFQ/profile-displayphoto-shrink_800_800/0/1595939105632?e=1724889600&v=beta&t=_pjNFXdW8VeM4IR5RhY9cgZ0NsAakg6EBEssgodCpwk" width="100px;" alt="Foto"/><br>
        <sub>
          <b>João Pedro Dias Caparroz</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<br>

## 😄 Contribute

To contribute [click here](/docs/CONTRIBUTING.md) | *not ready*