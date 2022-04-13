<template>
  <div>
    <b-form @submit="onSubmit" v-if="show">
      <b-form-group id="input-group-1" label="Nombre:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.first_name"
          placeholder="Ingresar Nombre"
          :maxlength="10"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Apellido:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.last_name"
          placeholder="Ingresar Apellido"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-6" label="Trayecto: " label-for="input-6">
        <b-form-select
          v-model="form.assigned_journey"
          :options="journey_options"
          @change="getBusesOptionOnJourney"
          required
        ></b-form-select>
      </b-form-group>
      <b-form-group id="input-group-7" label="Bus: " label-for="input-7">
        <b-form-select
          v-model="form.bus"
          :options="buses_options"
          :required="!createMode && buses_options.length > 0"
        ></b-form-select>
      </b-form-group>
      <b-button type="submit" variant="primary">{{
        createMode ? "Crear" : "Actualizar"
      }}</b-button>
    </b-form>
  </div>
</template>
<script>
export default {
  props: ["type", "data"],
  beforeMount() {
    // this.$store.commit("changeSpinner");
    this.getJourneys();
    // this.getDrivers()
    // this.$store.commit("changeSpinner");
  },
  data() {
    let prevData = { ...this.data };
    console.log(prevData);
    return {
      journey_options: [],
      buses_options: [],
      createMode: Object.keys(prevData).length === 0,
      form: {
        first_name: prevData.first_name,
        last_name: prevData.last_name,
        assigned_journey: prevData.journey_id,
        bus: prevData.bus_id
      },
      allData: prevData,

      show: true
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      let formData = { ...this.form };

      const agregarElemento = async () => {
        // let formData = {...this.form}
        // console.log(formData)
        formData["passenger_id"] = this.allData["passenger_id"];
        if (this.createMode) {
          await this.$store.dispatch("storeObject", {
            formData,
            type: this.type
          });
        } else {
          await this.$store.dispatch("updateObject", {
            formData,
            type: this.type
          });
        }
        // await this.$store.dispatch("storeObject", {
        //   formData,
        //   type: this.type
        // });
      };
      agregarElemento();
    },

    async getJourneys() {
      await this.$store
        .dispatch("fetchData", { type: "journeys" })
        .then(response => {
          let options = [];
          // console.log(response)
          for (let journey of response) {
            options.push({
              text: journey.journey_name,
              value: journey.journey_id
            });
          }
          this.journey_options = options;
        })
        .catch(error => {
          console.log(error);
        });
    },
    async getBusesOptionOnJourney() {
      await this.$store
        .dispatch("fetchData", {
          type: `journeys?element_id=${this.form.assigned_journey}`
        })
        .then(response => {
          let options = [];
          let buses = response[0].buses;
          for (let bus of buses) {
            options.push({ value: bus.bus_id, text: bus.plate });
          }
          this.buses_options = options;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
