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
          :maxlength="10"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-7" label="Fecha: " label-for="input-7">
        <b-form-datepicker
          id="input-7-datepicker"
          v-model="form.date"
          required
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group id="input-group-8" label="Hora: " label-for="input-8">
        <b-form-timepicker
          id="input-8-timepicker"
          v-model="form.hour"
          placeholder="Escoge una hora"
          locale="es"
        ></b-form-timepicker>
      </b-form-group>

      <b-form-group id="input-group-5" label="Destino: " label-for="input-5">
        <b-form-select
          v-model="form.from_city"
          :options="city_options"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group id="input-group-6" label="Origen: " label-for="input-6">
        <b-form-select
          v-model="form.to_city"
          :options="city_options"
          required
        ></b-form-select>
      </b-form-group>

      <b-form-group id="input-group-3" label="Bus: " label-for="input-3">
        <b-button class="mb-2" @click="agregarBus" variant="primary"
          >Agregar Bus</b-button
        >
        <div class="mb-2" v-for="busObj in form.busList" :key="busObj.bus_id">
          <b-form-select
            v-model="busObj.bus_id"
            :options="bus_options"
            required
          ></b-form-select>
        </div>
        <!-- <b-form-select
          v-model="form.assigned_bus"
          :options="bus_options"
          required
        ></b-form-select> -->
      </b-form-group>
      <!-- <b-form-group id="input-group-4" label="Conductor:" label-for="input-4">
        <b-form-select
          v-model="form.assigned_driver"
          :options="driver_options"
          required
        ></b-form-select>
      </b-form-group> -->
      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>
<script>
export default {
  props: ["type", "data"],
  beforeMount() {
    this.getBuses();
  },
  data() {
    let cities = [
      { value: "ciudad1", text: "ciudad1" },
      { value: "ciudad2", text: "ciudad2" },
      { value: "ciudad3", text: "ciudad3" },
      { value: "ciudad4", text: "ciudad4" },
      { value: "ciudad5", text: "ciudad5" },
      { value: "ciudad6", text: "ciudad6" }
    ];


    let prevData = { ...this.data };
    return {
      bus_options: [],
      driver_options: [],
      city_options: cities,
      form: {
        journey_name: prevData.journey_name,
        from_city: prevData.from_city,
        date: prevData.date,
        to_city: prevData.to_city,
        busList: [{ bus_id: -1 }],
        hour: ""
      },
      show: true
    };
  },
  methods: {
    agregarBus() {
      this.form.busList.push({ bus_id: -1 });
    },
    parseBusList(original_bus_list) {
      let bus_list = [];
      for (let bus of original_bus_list) {
        let busParsed = { ...bus };
        bus_list.push(busParsed);
      }
      return bus_list;
    },
    onSubmit(event) {
      event.preventDefault();
      let formData = { ...this.form };

      if (formData.date === "" || formData.hour === "") {
        alert("Determinar fecha y hora");
        return;
      }

      if (formData.from_city === formData.to_city) {
        alert("Elegir diferentes ciudades");
        return;
      }

      formData["date"] = `${formData.date} ${formData.hour}`;

      formData["busList"] = this.parseBusList(formData["busList"]);


      const agregarElemento = async () => {
        await this.$store.dispatch("storeObject", {
          formData,
          type: this.type
        });
      };

      try {
        agregarElemento();
      } catch (e) {
        console.log(e);
        return;
      }
    },
    onReset(event) {
      event.preventDefault();

      this.form.journey_name = "";
      this.form.from_city = "";
      this.form.to_city = "";
      this.form.date = "";
      this.form.hour = "";

      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },

    async getBuses() {
      await this.$store
        .dispatch("fetchData", { type: "buses?available=1" })
        .then(response => {
          let options = [];
          for (let bus of response) {
            options.push({ text: bus.plate, value: bus.bus_id });
          }
          this.bus_options = options;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
