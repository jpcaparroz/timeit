# How to Use

If you want to use **TimeiT**, you'll need to follow a few steps. Below, I explain how to do it:

<br>

# 1. Creating a Notion Integration

You need to create a new `integration` by following this link: [Notion Integration](https://www.notion.so/profile/integrations).

## Capabilities

The integration needs the following 3 `content` capabilities:

- Read content
- Update content
- Insert content

![integration-capabilities](../images/integration-capabilities.png)

## Token

You’ll need the integration token for your `.env` file.

![integration-token](../images/integration-token.png)

Copy it and place it in your `.env` file.

![token-example](../images/token-example.png)

<br>

# 2. Duplicate the TimeiT Template

You need to duplicate the TimeiT template from my Notion template using this link: [Notion TimeiT Template](https://joaocaparroz.notion.site/Timeit-107c7e9cee0e80f39c5afbf540906910).

![duplicate-arrow](../images/duplicate-arrow.png)

*You need to be logged in to duplicate.*

<br>

# 3. Give Access to the Integration

You need to grant access for your integration to your TimeiT page.

1. Go to `...` in the top right corner.
2. Go to `Connections`.
3. Click on `Connect to`.
4. Search for your integration name.
5. Done! =)

![access-tutorial](../images/access-integration.png)

<br>

# 4. Getting All Database IDs

You need to retrieve the IDs of all 3 databases from the Notion page.

![get-database-id](../images/get-database-id.png)

1. Go to any `database`.
2. Click `...` on the database title.
3. Click on `View database`.
4. Now you need to `copy` the database ID from your browser's URL.
   ![get-database-id-tutorial](../images/notion-database-id-tutorial.png)
5. Then, place the database ID in your `.env` file.
6. Repeat this for all 3 databases:
    - timeit
    - timeit-consolidated
    - timeit-historical
7. Done! =)

---

# Results

Your `.env` file will look like this:

![env-example](../images/env-example.png)
