<template>
<div id=app>
  <div class="jumbotron">
    <h1 class="display-4">Risk Creator</h1>
    <br><br>
    <h2>Create a new risk type</h2>
    Risk Type:
    <input type="text" placeholder="Car Insurance" v-model="risk_type">
  </div>

  <div class="container">
    <table class="table" v-show="rows.length > 0">
      <thead>
          <tr>
              <td><strong>Field Name</strong></td>
              <td><strong>Field Type</strong></td>
              <td><strong>Data</strong></td>
          </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in rows" v-bind:key="index">
            <td><input type="text" v-model="row.field_name_row"></td>
            <td>
                <select v-model="row.field_type_select_row">
                  <option v-for="option in options" v-bind:value="option.value" v-bind:key="option.id">
                    {{ option.text }}
                  </option>
                </select>
            </td>
            <div v-if="row.field_type_select_row==='Enum'">
              <td>
                <select v-model="row.field_data">
                  <option v-for="thing in things" v-bind:value="thing.value" v-bind:key="thing.id">
                    {{ thing.text }}
                  </option>
                  </select>
              </td>
            </div>
            <div v-else-if="row.field_type_select_row==='Text'">
              <td><input type="text" v-model="row.field_data"></td>
            </div>
            <div v-else-if="row.field_type_select_row==='Date'">
              <td><input type="date" v-model="row.field_data"></td>
            </div>
            <div v-else>
              <td><input type="text" v-model="row.field_data"></td>
            </div>
            <td>
                <button class="btn btn-danger" v-on:click="removeElement(index);" style="cursor: pointer">Remove</button>
            </td>
        </tr>
      </tbody>
    </table>
  </div>

  <p></p>

  <button class="button btn-primary" @click="addField">Add Field</button>
  <button class="button btn-success" @click="postRisk">Create Risk</button>

  <hr/>
  <h2>Current Risks in Database</h2>
  <div class="risk_list">
    <p v-if="risks && risks.length === 0">No Risks</p>
    <div class="risk" v-for="risk in risks" :key="risk.id">
      <p class="risk-type">Risk Type: <strong>{{risk.risk_type}}</strong>, with Fields:</p>
      <ul v-if="risk.fieldz && risk.fieldz.length">
          <li v-for="field of risk.fieldz" :key="field.id">
              <u>{{field.name}}</u> of type: <u>{{field.field_type}}</u>
          </li>
      </ul>
    </div>
  </div>
  <hr/>
</div>
  <!-- <ul v-if="errors && errors.length">
    <li v-for="error of errors" :key="error.id">
      {{error.message}}
    </li>
  </ul> -->
</template>

<script>
import axios from 'axios'

export default {
  // name: 'App',
  data () {
    return {
      options: [
        {text: 'Text', value: 'Text'},
        {text: 'Number', value: 'Number'},
        {text: 'Date', value: 'Date'},
        {text: 'Enum', value: 'Enum'}
      ],
      things: [
        {text: 'Option 1', value: 1},
        {text: 'Option 2', value: 2},
        {text: 'Option 3', value: 3}
      ],
      risks: [],
      errors: [],
      rows: [],
      risk_type: '',
      fieldz: []
    }
  },
  methods: {
    addField: function () {
      document.createElement('tr')
      this.rows.push({field_name_row: '', field_type_select_row: '', field_data: ''})
    },

    removeElement: function (index) {
      this.rows.splice(index, 1)
    },

    // GET the RiskList
    fetchRisks: function () {
      axios.get(`http://127.0.0.1:8000/api/risks/`).then(response => {
        // JSON responses are automatically parsed.
        this.risks = response.data
      })
        .catch(e => {
          this.errors.push(e)
        })

      // async / await version (created() becomes async created())
      //
      // try {
      //   const response = await axios.get(`http://127.0.0.1:8000/api/risks/`)
      //   this.risks = response.data
      // } catch (e) {
      //   this.errors.push(e)
      // }
    },

    // POST to create a new risk type
    postRisk: function () {
      this.rows.forEach((element) => {
        this.fieldz.push({name: element.field_name_row, field_type: element.field_type_select_row})
        console.log(element.field_name_row)
      })
      axios.post(`http://127.0.0.1:8000/api/risks/`, {
        risk_type: this.risk_type,
        fieldz: this.fieldz
      }).then(response => {
        this.fetchRisks()
        console.log(response)
      })
        .catch(e => {
          this.errors.push(e)
        })
    }
  },

  // Fetches risks when the component is created.
  created () {
    this.fetchRisks()
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.risk_list {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

.table {
  margin: 0 auto;
  max-width: 30%;
  text-align: center;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

</style>
