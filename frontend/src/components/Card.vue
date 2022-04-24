<template>
  <div>
    <b-col>
      <div v-if="type === 'drivers'">
        <driver-card
          :deleteFunction="deleteFunction"
          :parsedData="parsedData"
          :editContents="this.editContents"
        ></driver-card>
      </div>
      <div v-else-if="type === 'buses'">
        <bus-card
          :parsedData="parsedData"
          :editContents="this.editContents"
        ></bus-card>
      </div>
      <div v-else-if="type === 'journeys'">
        <journey-card
          :deleteFunction="deleteFunction"
          :parsedData="parsedData"
          :editContents="this.editContents"
        ></journey-card>
      </div>
      <div v-else-if="type === 'passengers'">
        <passenger-card
          :deleteFunction="deleteFunction"
          :parsedData="parsedData"
          :editContents="this.editContents"
        ></passenger-card>
      </div>
    </b-col>
  </div>
</template>

<script>
import BusCardVue from "./cardContents/BusCard.vue";
import DriverCard from "./cardContents/DriverCard.vue";
import JourneyCard from "./cardContents/JourneyCard.vue";
import PassengerCard from "./cardContents/Passenger.vue";

export default {
  props: ["data", "type", "id", "editContents"],
  components: {
    "driver-card": DriverCard,
    "bus-card": BusCardVue,
    "journey-card": JourneyCard,
    "passenger-card": PassengerCard
  },
  data() {
    return {
      parsedData: { ...this.data }
    };
  },
  methods: {
    deleteFunction() {
      const deleteReq = async () => {
        let object_ = { ...this.parsedData };

        let element_id_key = Object.keys(object_).filter(element => {
          if (element.indexOf("id") > -1) return element;
        });

        await this.$store.dispatch("deleteElement", {
          type: this.type,
          element_id: object_[element_id_key]
        });
      };
      deleteReq();
    }
  },
  computed: {
    modalId() {
      return `modal-${this.id}`;
    }
  }
};
</script>

<style scoped></style>
