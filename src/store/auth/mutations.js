import {
    SET_PRESCRIPTION
} from "../storeconstants";

export default {

    [SET_PRESCRIPTION](state, prescription) {
        state.prescription = prescription
    },
}