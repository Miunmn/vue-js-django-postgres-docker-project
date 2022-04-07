<template>
  <div>
    <b-form @submit="onSubmit"  v-if="show">
      <b-form-group
        id="input-group-1"
        label="Nombre:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.first_name"
          placeholder="Ingresar Nombre"
          :maxlength='10'
          required
          
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-2"
        label="Apellido:"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          v-model="form.last_name"
          placeholder="Ingresar Apellido"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-6" label="Trayecto: " label-for="input-6" >
        <b-form-select v-model="form.assigned_journey" :options="journey_options" required></b-form-select>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>
<script>
  export default {
    props: ['type'],
    beforeMount() {
        // this.$store.commit("changeSpinner");
        this.getJourneys()
        // this.getDrivers()
        // this.$store.commit("changeSpinner");
    },
    data() {
      return {
        journey_options: [],
        form: {
          first_name: '',
          last_name: '',
          assigned_journey: ''
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        let formData = {...this.form}

        const agregarElemento = async() =>{
            // let formData = {...this.form}
            // console.log(formData)
            await this.$store.dispatch("storeObject", { formData, type: this.type });
        }

        try {
            agregarElemento()
        }
        catch(e){
            console.log(e)
        } 
      },

      async getJourneys() {
        await this.$store.dispatch("fetchData",{ type: "journeys" }).then(response => {
            let options = []
            // console.log(response)
            for(let journey of response){
                options.push({text: journey.journey_name, value: journey.journey_id})
            }
            this.journey_options=options
        })
        .catch(error=>{
            console.log(error)
        })       
      },
    }
  }
</script>