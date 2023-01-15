import mutations from './mutations';
import getters from './getters';

export default {
    namespaced: true,
    state() {
        return {
            prescription: [
                {title: 'Cyclosporine', checked: false},
                {title: 'Tacrolimus', checked: true},
                {title: 'Imuran', checked: true}
            ]
        }
    },
    mutations,
    getters
}