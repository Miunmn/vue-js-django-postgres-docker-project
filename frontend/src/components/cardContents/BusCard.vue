<template>
  <div>
    <b-card
      :title="`${parsedData.plate}`"
      img-src="https://media.istockphoto.com/photos/white-passenger-bus-picture-id135327019?k=20&m=135327019&s=612x612&w=0&h=YJneXYFReSVuKSIFOy5wGIygeLeb1UquX4BWLk-MluI="
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 20rem;"
      class="mb-2"
      footer-tag="footer"
    >
      <div>
        <b-card-text>
          <strong>Años de servicio:</strong> {{ parsedData.years_of_service }}
        </b-card-text>
        <b-card-text v-if="parsedData.passengers">
          <strong>Pasajeros:</strong> {{ parsedData.passengers }}
        </b-card-text>
        <b-card-text>
          <strong>Capacidad:</strong> {{ parsedData.capacity }}
        </b-card-text>
        <div v-if="parsedData.driver">
          <b-card-text>
            <strong>Conductor:</strong> {{ parsedData.driver }}
          </b-card-text>
        </div>
      </div>
      <template #footer>
        <b-row align-h="between">
          <b-col cols="4">
            <b-button
              @click="handleEdit"
              href="#"
              v-b-modal.modal-2
              variant="primary"
            >
              Editar
            </b-button>
          </b-col>
          <b-col cols="4">
            <b-button @click="deleteFunction" href="#" variant="danger">
              Delete
            </b-button>
          </b-col>
        </b-row>
      </template>
    </b-card>
  </div>
</template>

<script>
// import ModalAddElement from "../ModalAddElement.vue";

export default {
  props: ["parsedData", "editContents"],
  data() {
    return {};
  },
  // components: { "modal-content": ModalAddElement },

  beforeMount() {
    console.log({ ...this.parsedData });
  },
  methods: {
    deleteFunction() {
      const deleteReq = async () => {
        let object_ = { ...this.parsedData };

        let element_id_key = "bus_id";

        console.log(element_id_key);
        await this.$store.dispatch("deleteElement", {
          type: "buses",
          element_id: object_[element_id_key]
        });
      };
      deleteReq();
    },
    handleEdit() {
      this.editContents(this.parsedData);
    }
  }
};
</script>
