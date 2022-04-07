<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Placa:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.plate"
          placeholder="Ingresar Placa"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-2" label="Años de servicio:" label-for="input-2">
        <b-form-input 
        id="`input-2`" 
        type="number"
        placeholder="Ingresar Años"
        v-model="form.years_of_service"
        required
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    props: ['type'],
    data() {
      return {
        form: {
          plate: '',
          years_of_service: ''
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        const agregarElemento = async() =>{
            console.log(this.form)

            let formData = JSON.parse(JSON.stringify(this.form))
            // console.log(formData)
            // await this.$store.dispatch("storeObject", { formData, type: this.type });
            await this.$store.dispatch("storeObject", { formData, type: this.type });            
            await this.$store.dispatch("fetchJobs",{ type: this.type });
        }

        agregarElemento()

      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        
        this.form.plate = ''
        this.form.years_of_service = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>