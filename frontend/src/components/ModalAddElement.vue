<template>
  <div v-if="type === 'drivers'">
    <driver-form :data="this.data" :type="this.type"></driver-form>
  </div>
  <div v-else-if="type === 'buses'">
    <bus-form :data="this.data" :type="this.type"></bus-form>
  </div>
  <div v-else-if="type === 'passengers'">
    <passenger-form :data="this.data" :type="this.type"></passenger-form>
  </div>
  <div v-else-if="type === 'journeys'">
    <journey-form :data="this.data" :type="this.type"> </journey-form>
  </div>
</template>

<script>
import Driver from "./modalContents/DriverModal.vue";
import Bus from "./modalContents/BusModal.vue";
import Passenger from "./modalContents/PassengerModal.vue";
import Journey from "./modalContents/JourneyModal.vue";

export default {
  props: ["type", "updateData"],
  components: {
    "driver-form": Driver,
    "bus-form": Bus,
    "passenger-form": Passenger,
    "journey-form": Journey
  },
  data() {
    let prevData_ =
      Object.keys({ ...this.updateData }).length === 0
        ? null
        : { ...this.updateData };
    return {
      data: prevData_
    };
  },
  methods: {}
};
</script>
