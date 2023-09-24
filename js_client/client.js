const contentContainer = document.getElementById("content-container")
const loginForm = document.getElementById("login-form")
const searchForm = document.getElementById("search-form")

const baseEndpoint = "http://localhost:8000/api"

if (loginForm) {
    loginForm.addEventListener("submit", handleLogin)
}

if (searchForm) {
    loginForm.addEventListener("submit", handleSearch)
}

function handleLogin(event) {
    // console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    // console.log(bodyStr,loginObjectData)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options)// This is called Promise in JS // Just like the py code : requests.post
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(authData=>{
        handleAuthData(authData, getProductList)
    }) 
    .catch(err=>{
        console.log(err)
    })

}   

function handleSearch(event) {
    event.preventDefault()
    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem('access') 
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`
    }
    const options = {
        method: "GET",
        headers: headers
    }
    fetch(endpoint, options) //  Promise
    .then(response=>{
        return response.json()
    })
    .then(data => {
        const validData = isTokenNotValid(data)
        if (validData && contentContainer){
            contentContainer.innerHTML = ""
            if (data && data.hits) {
                let htmlStr  = ""
                for (let result of data.hits) {
                    htmlStr += "<li>"+ result.title + "</li>"
                }
                contentContainer.innerHTML = htmlStr
                if (data.hits.length === 0) {
                    contentContainer.innerHTML = "<p>No results found</p>"
                }
            } else {
                contentContainer.innerHTML = "<p>No results found</p>"
            }
        }
    })
    .catch(err=> {
        console.log('err', err)
    })
}

function handleAuthData(authData, callback) {
    localStorage.setItem("access", authData.access) // setItem("key", "value")
    localStorage.setItem("refresh", authData.refresh) // setItem("key", "value")
    if (callback) {
        callback()
    }
    
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body) {
    return {
        method : method == null ? "GET" : method,
        headers : {
            "Content-Type" : "application/json",
            "Authorization" : `Bearer ${localStorage.getItem("access")}`
        },
        body : body ? body : null
    }
}

function validateJWTToken() {
    // fetch
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method : "POST",
        headers : {
            "Content-Type" : "application/json"
        },
        body : JSON.stringify({
            token : localStorage.getItem("access")
        })
    }
    fetch(endpoint, options)
    .then(response=>response.json())
    .then(x =>{
        isTokenNotValid(x)
        console.log(x)
    })
}

function isTokenNotValid(jsonData) {
    if (jsonData && jsonData.code == "token_not_valid") {
        // run a refresh token fetch
        alert("Please login again")
        return false
    }
    return true
}
function getProductList() {
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()
    fetch(endpoint, options)
    .then(response=>{
        console.log(response)
        response.json()
    })
    .then(data=>{ 
        const validData = isTokenNotValid(data)
        console.log(data)
        if (validData) {
        writeToContainer(data)
        }
    })
}

validateJWTToken()


const searchClient = algoliasearch('ZXMBVCXQCZ', '7c6110b5b202c3690e2dda9ffe14ed83');

const search = instantsearch({
  indexName: 'amirh-far_Product',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),

  instant.widgets.clearRefinements({
    container: "#clear-refinements",

  }),
  

  instant.widgets.refinementsList({
    container: "#user-list",
    attribue: "user"
  }),


  instant.widgets.refinementsList({
    container: "#public-list",
    attribue: "public"

  }),
  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
        item: `<div>
                    <div>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</div>
                    <div>{{#helpers.highlight}}{ "attribute": "body" }{{/helpers.highlight}}</div>
                    <p>{{ user  }}</p>
                    <p>\$ {{ price }}</p>
              </div>`
    }
  })
]);

search.start();
