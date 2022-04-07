<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Nombre de Trayecto:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.journey_name"
          placeholder="Ingresar Nombre de Trayecto"
          :maxlength='10'
          required
          
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-7" label="Fecha: " label-for="input-7">
          <b-form-datepicker id="input-7-datepicker" v-model="form.date" required></b-form-datepicker>
      </b-form-group>

      <b-form-group id="input-group-8" label="Hora: " label-for="input-8">
        <b-form-timepicker id="input-8-timepicker" v-model="form.hour" placeholder="Escoge una hora" locale="es"></b-form-timepicker>
      </b-form-group>

      <b-form-group id="input-group-5" label="Destino: " label-for="input-5" >
        <b-form-select v-model="form.from_city" :options="city_options" required></b-form-select>
      </b-form-group>
      

      <b-form-group id="input-group-6" label="Origen: " label-for="input-6" >
        <b-form-select v-model="form.to_city" :options="city_options" required></b-form-select>
      </b-form-group>
      <b-form-group id="input-group-3" label="Bus: " label-for="input-3" >
        <b-form-select v-model="form.assigned_bus" :options="bus_options" required></b-form-select>
      </b-form-group>
      <b-form-group id="input-group-4" label="Conductor:" label-for="input-4" >
        <b-form-select v-model="form.assigned_driver" :options="driver_options" required></b-form-select>
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
        this.getBuses()
        this.getDrivers()
        // this.$store.commit("changeSpinner");
    },
    data() {
    //   this.getData()
      let cities = [
          {value: 'ciudad1', text: 'ciudad1'},
          {value: 'ciudad2', text: 'ciudad2'},
          {value: 'ciudad3', text: 'ciudad3'},
          {value: 'ciudad4', text: 'ciudad4'},
          {value: 'ciudad5', text: 'ciudad5'},
          {value: 'ciudad6', text: 'ciudad6'}
      ];
      return {
        bus_options: [],
        driver_options: [],
        city_options: cities,
        form: {
          journey_name: '',
          from_city: '',
          date: '',
          to_city: '',
          hour: '',
          assigned_bus: '',
          assigned_driver: ''
        },
        show: true
      }
    },
    // watch: {
    //    bus_options(val){
    //        console.log("aaa",val)
    //    }
    // },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        let formData = {...this.form}

        if(formData.date === "" || formData.hour === ""){
          alert("Determinar fecha y hora")
          return
        }

        formData['date'] = `${formData.date} ${formData.hour}`

        // console.log(formData)

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
            return
        } 
        
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        
        this.form.journey_name = ''
        this.form.from_city = ''
        this.form.to_city = ""
        this.form.assigned_bus = ""
        this.form.assigned_driver = ""
        this.form.date = ""
        this.form.hour = ""

        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },

      async getBuses() {
        await this.$store.dispatch("fetchData",{ type: "buses" }).then(response => {
            let options = []
            // console.log(response)
            for(let bus of response){
                options.push({text: bus.plate, value: bus.bus_id})
            }
            this.bus_options=options
        })
        .catch(error=>{
            console.log(error)
        })       
      },
      async getDrivers() {
        await this.$store.dispatch("fetchData",{ type: "drivers" }).then(response => {
            let options = []
            for(let driver of response){
                options.push({text: `${driver.first_name} ${driver.last_name}`, value: driver.driver_id})
            }
            this.driver_options=options
        })
        .catch(error=>{
            console.log(error)
        })       
      },
    }
  }
</script>