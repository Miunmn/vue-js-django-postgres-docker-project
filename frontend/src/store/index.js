import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
// import { resolve,reject } from "core-js/fn/promise";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    rows: 0,
    dataList: [],
    showSpinner: false
  },
  mutations: {
    SET_DATA(state, dataList) {
      state.dataList = dataList;
    },
    SET_ROWS(state, rows) {
      state.rows = rows;
    },

    SET_SPINNER(state, spinner) {
      state.showSpinner = spinner;
    }
  },
  actions: {
    changeSpinner({ commit }) {
      let current_spinner = this.state.showSpinner;
      commit("SET_SPINNER", !current_spinner);
    },
    async storeObject({ commit, dispatch }, { formData, type }) {
      // console.log(dispatch, formData)
      commit("SET_SPINNER", true);
      new Promise(async resolve => {
        await axios
          .post(`http://127.0.0.1:8000/${type}`, formData, {
            headers: { "content-type": "text/plain" }
          })
          .then(async respuesta => {
            await dispatch("fetchData", { type }).then(myJson => {
              commit("SET_DATA", myJson);

              resolve(respuesta);
              commit("SET_SPINNER", false);
            });
          })
          .catch(error => {
            if (error.response.status === 400) {
              alert(error.response.data);
            }
          });
      });
    },
    async deleteElement({ commit, dispatch }, { type, element_id }) {
      console.log("type, element_id", type, element_id);
      commit("SET_SPINNER", true);
      let request = new Promise(async resolve => {
        // console.log('ejecutar')
        const res = await axios.delete(
          `http://127.0.0.1:8000/${type}?element_id=${element_id}`,
          { headers: { "content-type": "text/plain" } }
        );

        //Hacer request de la lista de elementos
        const myJson = await dispatch("fetchData", { type });
        commit("SET_DATA", myJson);

        resolve(res);
        commit("SET_SPINNER", false);
      });
      request.catch(error => {
        console.log(error);
        alert("Error al tratar de elimina");
      });
    },
    async fetchData({ commit }, { type }) {
      // console.log("3f2f23323f243gg34g34g4343g", type);
      commit("SET_SPINNER", true);
      return new Promise(resolve => {
        setTimeout(async () => {
          const res = await axios.get(`http://127.0.0.1:8000/${type}`, {
            headers: { "content-type": "text/plain" }
          });
          let val = JSON.parse(res.data.dataList);
          resolve(val);
          commit("SET_SPINNER", false);
        });
      });
    },
    async updateObject({ commit, dispatch }, { formData, type }) {
      commit("SET_SPINNER", true);
      return new Promise(async resolve => {
        await axios
          .put(`http://127.0.0.1:8000/${type}`, formData, {
            headers: { "content-type": "text/plain" }
          })
          .then(async response => {
            alert(response.data.mensaje);

            await dispatch("fetchData", { type }).then(myJson => {
              commit("SET_DATA", myJson);

              resolve(response);
              commit("SET_SPINNER", false);
            });
          })
          .catch(error => {
            if (error.response.status === 400) {
              alert(error.response.data);
            }
          });
      });
    },
    async fetchJobs({ commit, dispatch }, { type }) {
      // console.log("type", type)
      const myJson = await dispatch("fetchData", { type });
      commit("SET_DATA", myJson);

      // dispatch("updatePagination", { myJson, currentPage: 1, perPage: 3 });
      return myJson;
    }
  },
  getters: {
    getDataList(state) {
      return function() {
        return state.dataList;
      };
    },
    getRows(state) {
      return state.rows;
    },
    getSpinner(state) {
      return function() {
        state.showSpinner;
      };
    }
  },
  modules: {}
});
