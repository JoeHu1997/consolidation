`POST`

`url` : `/compression`

```json
request
{
	a: 123,
	b: 1234,
	c: 324234
}


response
{
	result: 234324,
}
```


utility functions -> backend endpoints -> frontend make api calls -> render corresponding data -> display chart

1. backend framework
	- fastAPI
	- flask
2. deployment -> `url` -> postman `POST` `https://test.com/consolidation` 
	- [fly.io](https://fly.io/docs/)
	- [render.com](https://render.com/)
3. frontend framework -> Javascript + HTML + CSS -> deployment
	- without framework
	- jQuery
	- react/vue...
4. Integration -> frontend + backend -> data, e.g. chart, table -> library/package


```json

{
  "calculatetype": ["A"],
  "soil": [{
    "soiltype": string[],
    "thickness": number[],
    "e": number | null,
    "Gs": number[],
    "w": null,
    "S": null,
    "gammad": null,
    "gammam": null
  }, {
    "soiltype": ["A"],
    "thickness": [11],
    "e": null,
    "Gs": null,
    "w": null,
    "S": null,
    "gammad": null,
    "gammam": null
  }],
}

```

```javascript
const data = reponse.json()
const soil = data.soil
console.log(soil)

// [{solitype: ["C"], tickness: [10]...}]

const firstSoil = soil[0]
const secondSoil = soil[1]
```