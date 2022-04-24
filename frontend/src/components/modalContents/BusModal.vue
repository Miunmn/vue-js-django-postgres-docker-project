<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group-1" label="Placa:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.plate"
          placeholder="Ingresar Placa"
          required
          :disabled="!createMode"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        id="input-group-2"
        label="Años de servicio:"
        label-for="input-2"
      >
        <b-form-input
          id="`input-2`"
          type="number"
          placeholder="Ingresar Años"
          v-model="form.years_of_service"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group
        id="input-group-3"
        label="Capacidad de Pasajeros:"
        label-for="input-3"
      >
        <b-form-input
          id="`input-3`"
          type="number"
          placeholder="Ingresar Años"
          v-model="form.capacity"
          required
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-4" label="Conductor:" label-for="input-4">
        <b-form-select
          v-model="form.driver"
          :options="driver_options"
          :required="!createMode && driver_options.length > 0"
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
  data() {
    let prevData = { ...this.data };
    return {
      driver_options: [],
      createMode: Object.keys(prevData).length === 0,
      form: {
        plate: prevData.plate,
        years_of_service: prevData.years_of_service,
        driver: prevData.driver,
        capacity: prevData.capacity
      },
      show: true
    };
  },
  beforeMount() {
    this.getDrivers();
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const asyncRequestFunction = async () => {
        let formData = JSON.parse(JSON.stringify(this.form));

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
      };

      asyncRequestFunction();
    },
    onReset(event) {
      event.preventDefault();

      this.form.plate = "";
      this.form.years_of_service = "";
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    async getDrivers() {
      await this.$store
        .dispatch("fetchData", { type: "drivers?available=1" })
        .then(response => {
          let options = [];
          for (let driver of response) {
            options.push({
              text: `${driver.first_name} ${driver.last_name}`,
              value: driver.driver_id
            });
          }
          this.driver_options = options;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
