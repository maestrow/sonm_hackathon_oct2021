const express = require('express')

const app = express()
const port = 1526

// parse application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: false }))

// parse application/json
app.use(express.json())

app.get('/get_task', (req, res) => {
  const task = {
    id: 1,
    a: 12,
    b: 8
  }

  res.setHeader('Content-Type', 'application/json');
  res.end(JSON.stringify(task));
})

app.post('/push_result', (req, res) => {
  console.log('you posted:\n')
  console.log(JSON.stringify(req.body, null, 2))
  res.sendStatus(200);
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})