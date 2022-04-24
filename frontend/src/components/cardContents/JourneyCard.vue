<template>
  <b-card
    :title="`${this.parsedData.journey_name} id: ${this.parsedData.journey_id}`"
    img-src="https://thumbs.dreamstime.com/z/model-travel-bus-map-london-travelling-bus-concept-conceptual-image-travel-tourism-model-travel-bus-108507278.jpg"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      <strong>Origen:</strong>
      {{ parsedData.from_city }}
    </b-card-text>
    <b-card-text>
      <strong>Destino: </strong> {{ parsedData.to_city }}
    </b-card-text>
    <b-card-text>
      <strong> Cantidad Promedio de Pasajeros: </strong>
      {{ parsedData.passengers }}
    </b-card-text>
    <b-card-text>
      <strong>Fecha:</strong>
      {{ date }}
    </b-card-text>
    <b-card-text>
      <strong> Buses:</strong>
      <div :key="bus.bus_id" v-for="bus in parsedData.buses">
        <!-- Placa: {{ bus.plate }} Pasajeros: {{bus.number_passengers}} Capacidad: {{ bus.capacity }} -->
        <b-container class="mb-3">
          <b-row align-h="center">
            <strong> {{ bus.plate }}</strong>
          </b-row>
          <b-row align-h="center">
            <b-col cols="6">Pasajeros: {{ bus.number_passengers }}</b-col>
            <b-col cols="6">Capacidad: {{ bus.capacity }}</b-col>
          </b-row>
        </b-container>
      </div>
      <!-- {{ parsedData.assigned_bus_id }} -->
    </b-card-text>
    <template #footer>
      <b-row align-h="between">
        <!-- <b-col cols="4">
          <b-button @click="handleEdit" v-b-modal.modal-2 variant="primary">Editar</b-button>
        </b-col> -->
        <b-col cols="4">
          <b-button @click="deleteFunction" href="#" variant="danger"
            >Delete</b-button
          >
        </b-col>
      </b-row>
    </template>
  </b-card>
</template>

<script>
export default {
  props: ["parsedData", "deleteFunction", "editContents"],
  beforeMount() {
    this.parseDate();
  },
  methods: {
    parseDate() {
      let date = new Date(this.parsedData.date);
      var options = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric"
      };
      this.date = date.toLocaleTimeString("es-ES", options);
    },
    handleEdit() {
      this.editContents(this.parsedData);
    }
  },

  data() {
    return {
      date: ""
    };
  }
};
</script>
