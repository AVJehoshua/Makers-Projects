const express = require('express')
const Thermostat = require('./thermostat')
const app = express()
const port = 3000


const thermostat = new Thermostat


app.get('/temperature', (req, res) => {
  const result = JSON.stringify(thermostat.getTemperature())
  res.send(`The temperature is ${result}`)
})

app.post('/up', (req, res) => {
  const result = JSON.stringify(thermostat.up())
  res.send(`The temperature is now: ${result}`)
})

app.post('/down', (req, res) => {
  const result = JSON.stringify(thermostat.down())
  res.send(`The temperature is now: ${result}`)
})

app.delete('/temperature', (req, res) => {
  const result = JSON.stringify(thermostat.reset())
  res.send(`The temperature is has been reset to: ${result}`)
})


console.log(`Server Listening on port: ${port}`)
app.listen(port)