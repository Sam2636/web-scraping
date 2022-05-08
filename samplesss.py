



import requests, json

endpoint = "https://graphql.epicgames.com/graphql"

query = {
    "query": "\n        query catalogQuery(\n            $productNamespace:String!,\n            $offerId:String!,\n            $locale:String,\n            $country:String!,\n            $lineOffers: [LineOfferReq]!) {\n                Catalog {\n                    catalogOffer(namespace: $productNamespace,\n                        id: $offerId,\n                        locale: $locale) {\n                            namespace\n                            effectiveDate\n                            id\n                            customAttributes {\n                                key\n                                value\n                            }\n                            items {\n                                id\n                                status\n                                customAttributes {\n                                    key\n                                    value\n                                }\n                            }\n                    }\n                }\n                PriceEngine {\n                    price(country: $country, lineOffers: $lineOffers) {\n                        totalPrice {\n                            discountPrice\n                            originalPrice\n                            voucherDiscount\n                            discount\n                            currencyCode\n                            currencyInfo {\n                                decimals\n                            }\n                            fmtPrice(locale: $locale) {\n                                originalPrice\n                                discountPrice\n                                intermediatePrice\n                            }\n                        }\n                        lineOffers {\n                            appliedRules {\n                                endDate\n                                discountSetting {\n                                    discountType\n                                }\n                            }\n                        }\n                    }\n                }\n            }\n        ",
    "variables": {
        "productNamespace": "cosmos",
        "offerId": "1c55202badfc4212b4f82553d5d22c3e", # This is found in the first request we made,
        "locale": "en-US",                             # data.Storefront.storefrontModules[1].offers[""0""].id to be more precise.
        "country": "US",
        "lineOffers": [{
            "offerId": "1c55202badfc4212b4f82553d5d22c3e", # The same id goes here too.
            "quantity": 1
        }],
        "calculateTax": False}
    }

data = requests.post(endpoint, headers={"Content-type": "application/json;charset=UTF-8"
                                       }, data=json.dumps(query)) # We added json.dumps because it basically turns dictionary
                                                                  # into JSON string.
print(data.json())