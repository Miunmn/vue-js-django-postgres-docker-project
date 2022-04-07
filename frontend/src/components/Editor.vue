<template>
    <div>
        <b-modal id="modal-1" :title="`Agregar un ${getElementName()}`">
            <modal-content :type="this.type"></modal-content>
        </b-modal>
        <b-container class="bv-example-row">
            <b-row class="text-center mb-3">
                <b-col><b-button variant="success" href="/journeys">Trayectos</b-button></b-col>
                <b-col><b-button variant="success" href="/passengers">Pasajeros</b-button></b-col>
                <b-col><b-button variant="success" href="/drivers">Conductores</b-button></b-col>
                <b-col><b-button variant="success" href="/buses">Buses</b-button></b-col>
            </b-row>
            <b-row class="text-center mb-5">
                <b-col  cols="auto"><b-button v-b-modal.modal-1 variant="outline-primary">Agregar</b-button></b-col>
            </b-row>

            <b-row>
                <b-col>
                    <b-row align-v="center">
                        <card 
                        :data="element"
                        :type="type"
                        :id="element.id"
                        v-for="element in getDataList"
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
import ModalAddElement from "./ModalAddElement.vue"
import { mapGetters } from "vuex";

export default {
    name: "editor",
    components: { "card": Card, "modal-content": ModalAddElement },
    computed: {
        ...mapGetters(["getRows", "getDataList"])
    },
    beforeMount() {
        this.type=this.$route.params.type;
        this.getRecords()
    },
    data() {
        return {
        currentPage: 1,
        perPage: 3
        };
    },
    methods: {
        async getRecords() {
            await this.$store.dispatch("fetchJobs",{ type: this.type });
        },
        parseElementData(elementData){
            return JSON.parse(elementData)
        },
        getElementName(){
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
                    return ""
            }
        }
  }
}
</script>


<style lang="scss">

</style>