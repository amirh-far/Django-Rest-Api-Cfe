const loginForm = document.getElementById("login-form")
const baseEndpoint = "http://localhost:8000/api"
if (loginForm) {
    loginForm.addEventListener("submit", handleLogin)
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
            "ContentType": "application/json"
        },
        body: ""
    }
    fetch(loginEndpoint, options)// This is called Promise in JS // Just like the py code : requests.post
    .then(response=>{
        console.log(response)
        return response.json()
    })
    .then(x =>{
        console.log(x)
    })
    .catch(err=>{
        console.log(err)
    })

}   