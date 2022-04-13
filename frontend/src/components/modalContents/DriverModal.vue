<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="input-group-1" label="Nombre:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.first_name"
          placeholder="Ingresar Nombre"
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

      <b-form-group id="input-group-3" label="Age:" label-for="input-3">
        <b-form-input
          id="`input-3`"
          type="number"
          placeholder="Ingresar Edad"
          v-model="form.age"
          required
        ></b-form-input>
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
    console.log(prevData);

    return {
      createMode: Object.keys(prevData).length === 0,
      form: {
        first_name: prevData.first_name,
        last_name: prevData.last_name,
        age: prevData.age
      },
      allData: prevData,
      show: true
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const agregarElemento = async () => {
        this.form["age"] = parseInt(this.form["age"]);

        let formData = JSON.parse(JSON.stringify(this.form));
        formData["driver_id"] = this.allData["driver_id"];

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

      try {
        agregarElemento();
      } catch (e) {
        console.log(e);
      }
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values

      this.form.first_name = "";
      this.form.last_name = "";
      this.form.age = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
};
</script>
