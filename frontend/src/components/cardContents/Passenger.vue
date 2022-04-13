<template>
  <b-card
    :title="`${this.parsedData.first_name} ${this.parsedData.last_name}`"
    img-src="https://previews.123rf.com/images/dolgachov/dolgachov1901/dolgachov190100734/115184774-group-of-happy-passengers-travelling-by-bus.jpg"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
    footer-tag="footer"
  >
    <b-card-text>
      <strong> Trayecto:</strong>
      {{ parsedData.journey_name }}
    </b-card-text>
    <b-card-text>
      <strong> Bus:</strong>
      {{ parsedData.bus_plate }}
    </b-card-text>
    <template #footer>
      <b-row align-h="between">
        <b-col cols="4">
          <b-button
            @click="handleEdit"
            href="#"
            v-b-modal.modal-2
            variant="primary"
            >Edit</b-button
          >
        </b-col>
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
  props: ["parsedData", "editContents"],
  methods: {
    deleteFunction() {
      const deleteReq = async () => {
        let object_ = { ...this.parsedData };

        let element_id_key = "passenger_id";

        console.log(element_id_key);
        await this.$store.dispatch("deleteElement", {
          type: "passengers",
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
