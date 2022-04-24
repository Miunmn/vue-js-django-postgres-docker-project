<template>
  <div>
    <b-modal id="modal-1" :title="`Agregar un ${getElementName()}`">
      <modal-content :type="this.type"></modal-content>
    </b-modal>
    <b-modal id="modal-2" :title="`Actualizar valores`">
      <modal-content
        :updateData="this.prevData"
        :type="this.type"
      ></modal-content>
    </b-modal>
    <b-container>
      <b-row class="mb-5">
        <b-nav content-class="tabs">
          <b-nav-item href="/journeys">Trayectos</b-nav-item>
          <b-nav-item href="/passengers">Pasajeros</b-nav-item>
          <b-nav-item href="/buses">Buses</b-nav-item>
          <b-nav-item href="/drivers">Conductores</b-nav-item>
        </b-nav>
      </b-row>
      <b-row class="mb-5">
        <b-col cols="3">
          <b-button v-b-modal.modal-1 variant="light">
            Agregar
          </b-button>
        </b-col>
        <b-col cols="5">
          <h3 class="title">
            {{
              `${this.getElementName()[0].toUpperCase() +
                this.getElementName().slice(1)}`
            }}
          </h3>
        </b-col>
        <b-col md="4">
          <b-navbar-nav label-cols-lg="2" class="ml-auto">
            <b-nav-form @submit.prevent="search">
              <b-form-input
                size="xl"
                class="mr-sm-2"
                placeholder="Ingresar"
                v-model="searchText"
              ></b-form-input>
              <b-button
                size="sm"
                variant="primary"
                class="my-2 my-sm-0"
                type="submit"
                >Buscar</b-button
              >
            </b-nav-form>
          </b-navbar-nav>
        </b-col>
      </b-row>
      <b-row class="mb-4">
        <b-col md="6" offset-md="3">
          <div v-if="this.type === 'journeys'">
            <b-navbar-nav label-cols-lg="2" class="ml-auto">
              <b-nav-form @submit.prevent="search">
                <p class="title">
                  Filtra a todos los buses de un trayecto con más del
                  {{ cantidad }}% de su capacidad vendida.
                </p>
                <b-form-group
                  label-for="input-formatter"
                  description="Porcentaje %"
                  class="mb-0"
                >
                  <b-form-input
                    size="xl"
                    class="mr-sm-2"
                    placeholder="Porcentaje"
                    id="input-formatter"
                    :min="0"
                    :max="100"
                    type="number"
                    v-model="cantidad"
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                  label-for="journey-id-input"
                  description="Id de Trayecto"
                >
                  <b-form-input
                    size="xl"
                    class="mr-sm-2"
                    type="number"
                    placeholder="Trayecto"
                    v-model="idTrayectoSearch"
                  ></b-form-input>
                </b-form-group>

                <b-button
                  size="sm"
                  variant="primary"
                  id="journey-id-input"
                  class="my-2 my-sm-0"
                  :disabled="idTrayectoSearch === '' || cantidad === ''"
                  @click="filterBuses"
                  >Consultar</b-button
                >

                <b-button
                  v-if="filtered_buses.length != 0"
                  size="sm"
                  variant="primary"
                  id="journey-id-input"
                  class="my-2 my-sm-0"
                  @click="limpiarBusqueda"
                  >Limpiar Búsqueda</b-button
                >
              </b-nav-form>
            </b-navbar-nav>
          </div>
        </b-col>
      </b-row>
      <b-row class="text-center mb-5">
        <card
          :data="element"
          :type="'buses'"
          :id="element.id"
          v-for="element in this.filtered_buses"
          :key="element.id"
        ></card>
      </b-row>
      <b-row class="text-center mb-5">
        <b-col>
          <b-row align-v="center">
            <card
              :data="element"
              :type="type"
              :editContents="editContents"
              :id="element.id"
              v-for="element in getDataListFunction"
              :key="element.id"
            ></card>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Card from "./Card.vue";
import ModalAddElement from "./ModalAddElement.vue";
import { mapGetters } from "vuex";
import axios from "axios";
export default {
  name: "editor",
  components: { card: Card, "modal-content": ModalAddElement },
  computed: {
    ...mapGetters(["getRows"]),
    getDataListFunction() {
      return this.$store.getters.getDataList();
    }
  },
  beforeMount() {
    this.type = this.$route.params.type;
    this.getRecords();
  },
  data() {
    return {
      currentPage: 1,
      perPage: 3,
      cantidad: 50,
      filtered_buses: [],
      idTrayectoSearch: "",
      searchText: "",
      prevData: null
    };
  },
  methods: {
    async getRecords() {
      await this.$store.dispatch("fetchJobs", { type: this.type });
    },
    clickTab(val) {
      this.$router.go(`/${val}`);
    },
    parseElementData(elementData) {
      return JSON.parse(elementData);
    },
    getElementName() {
      switch (this.type) {
        case "drivers":
          return "conductor";
        case "journeys":
          return "trayecto";
        case "buses":
          return "bus";
        case "passengers":
          return "pasajero";
        default:
          return "";
      }
    },
    parseNum(scope) {
      if (parseInt(scope.value) > 100) scope.value = 100;
      if (isNaN(parseInt(scope.value))) scope.value = 0;
    },
    filterBuses() {

      const fetchBuses = async () => {
        this.filtered_buses = [];
        axios
          .get(
            `http://127.0.0.1:8000/journeys-buses-filter?journey_id=${this.idTrayectoSearch}&percentage=${this.cantidad}`
          )
          .then(response => {
            let buses = JSON.parse(response.data.dataList);
            this.filtered_buses = buses;
          })
          .catch(error => {
            console.log(error);
            if (error.response.status === 400) {
              alert(error.response.data);
            }
          });
      };
      fetchBuses();
    },
    limpiarBusqueda() {
      this.filtered_buses = [];
    },
    editContents(data) {
      this.prevData = data;
    }
  }
};
</script>

<style lang="scss">
a {
  color: white !important;
}
.text-muted {
  color: white !important;
}

.title {
  color: white;
}
</style>
