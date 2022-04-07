import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
// import { resolve,reject } from "core-js/fn/promise";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        rows:0,
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
        changeSpinner({commit}){
          let current_spinner = this.state.showSpinner
          commit("SET_SPINNER", !current_spinner)
        },
        async storeObject({commit}, {formData, type}){
          // console.log(dispatch, formData)
          commit("SET_SPINNER", true);
          let res =  new Promise(async(resolve)=> {
            const respuesta =  await axios.post(`http://127.0.0.1:8000/${type}`, formData, { headers: { 'content-type': 'text/plain', } })
            resolve(respuesta)
            commit("SET_SPINNER", false);
          })
          res.catch(error=>{
            console.log(error)
          })          
        },
        async deleteElement({commit}, {type, element_id}){
          console.log("type, element_id", type, element_id)
          commit("SET_SPINNER", true)
          let request = new Promise(async(resolve)=> {
                // console.log('ejecutar')
                const res = await axios.delete(`http://127.0.0.1:8000/${type}?element_id=${element_id}`, { headers: { 'content-type': 'text/plain', } })

                resolve(res)
                commit("SET_SPINNER", false)
          }) 
          request.catch(error=>{
            console.log(error)
          }) 
        },
        async fetchData({commit}, {type}){
            console.log("3f2f23323f243gg34g34g4343g", type)
            commit("SET_SPINNER", true);
            return new Promise(resolve => {
                setTimeout(async () => {
                  const res = await axios.get(`http://0.0.0.0:8000/${type}`, { headers: { 'content-type': 'text/plain', } })
                    let val = JSON.parse(res.data.dataList)
                    resolve(val)
                    commit("SET_SPINNER", false);
                }
                )
            })
        },
        async fetchJobs({ commit, dispatch }, {type}) {
          // console.log("type", type)
          const myJson = await dispatch("fetchData", {type});
          commit("SET_DATA", myJson);

          // dispatch("updatePagination", { myJson, currentPage: 1, perPage: 3 });
          return myJson;
        },


    },
    getters: {
        getDataList(state){
            return state.dataList
        },
        getRows(state) {
          return state.rows;
        },
        getSpinner(state) {
          return state.showSpinner
        }
    },
    modules: {}
})


