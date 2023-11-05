import RegistrationForm from "@/components/registration/RegistrationForm.vue";
import { __VLS_publicComponent, __VLS_internalComponent, __VLS_componentsOption, __VLS_name } from "./RegistrationPageView.vue";

function __VLS_template() {
let __VLS_ctx!: InstanceType<__VLS_PickNotAny<typeof __VLS_publicComponent, new () => {}>> & InstanceType<__VLS_PickNotAny<typeof __VLS_internalComponent, new () => {}>> & {};
/* Components */
let __VLS_localComponents!: NonNullable<typeof __VLS_internalComponent extends { components: infer C; } ? C : {}> & typeof __VLS_componentsOption & typeof __VLS_ctx;
let __VLS_otherComponents!: typeof __VLS_localComponents & __VLS_GlobalComponents;
let __VLS_own!: __VLS_SelfComponent<typeof __VLS_name, typeof __VLS_internalComponent & typeof __VLS_publicComponent & (new () => { $slots: typeof __VLS_slots; })>;
let __VLS_components!: typeof __VLS_otherComponents & Omit<typeof __VLS_own, keyof typeof __VLS_otherComponents>;
/* Style Scoped */
type __VLS_StyleScopedClasses = {} &
{ 'root'?: boolean; } &
{ 'container'?: boolean; };
let __VLS_styleScopedClasses!: __VLS_StyleScopedClasses | keyof __VLS_StyleScopedClasses | (keyof __VLS_StyleScopedClasses)[];
/* CSS variable injection */
/* CSS variable injection end */
let __VLS_templateComponents!: {} &
__VLS_WithComponent<'trnasition', typeof __VLS_components, "Trnasition", "trnasition", "trnasition"> &
__VLS_WithComponent<'RegistrationForm', typeof __VLS_components, "RegistrationForm", "RegistrationForm", "RegistrationForm">;
({} as __VLS_IntrinsicElements).div; ({} as __VLS_IntrinsicElements).div; ({} as __VLS_IntrinsicElements).div; ({} as __VLS_IntrinsicElements).div;
__VLS_components.Trnasition; __VLS_components.Trnasition; __VLS_components.trnasition; __VLS_components.trnasition;
// @ts-ignore
[trnasition, trnasition,];
__VLS_components.RegistrationForm;
// @ts-ignore
[RegistrationForm,];
{
const __VLS_0 = ({} as __VLS_IntrinsicElements)["div"];
const __VLS_1 = __VLS_asFunctionalComponent(__VLS_0, {});
({} as __VLS_IntrinsicElements).div;
({} as __VLS_IntrinsicElements).div;
const __VLS_2 = __VLS_1({ ...{}, class: ("root"), }, ...__VLS_functionalComponentArgsRest(__VLS_1));
const __VLS_3 = __VLS_pickFunctionalComponentCtx(__VLS_0, __VLS_2)!;
{
const __VLS_4 = ({} as __VLS_IntrinsicElements)["div"];
const __VLS_5 = __VLS_asFunctionalComponent(__VLS_4, {});
({} as __VLS_IntrinsicElements).div;
({} as __VLS_IntrinsicElements).div;
const __VLS_6 = __VLS_5({ ...{}, class: ("container"), }, ...__VLS_functionalComponentArgsRest(__VLS_5));
const __VLS_7 = __VLS_pickFunctionalComponentCtx(__VLS_4, __VLS_6)!;
{
const __VLS_8 = __VLS_templateComponents['trnasition'];
const __VLS_9 = __VLS_asFunctionalComponent(__VLS_8, new __VLS_8({ ...{}, name: ("fade"), mode: ("out-in"), }));
__VLS_templateComponents.trnasition;
__VLS_templateComponents.trnasition;
const __VLS_10 = __VLS_9({ ...{}, name: ("fade"), mode: ("out-in"), }, ...__VLS_functionalComponentArgsRest(__VLS_9));
const __VLS_11 = __VLS_pickFunctionalComponentCtx(__VLS_8, __VLS_10)!;
{
const __VLS_12 = __VLS_templateComponents['RegistrationForm'];
const __VLS_13 = __VLS_asFunctionalComponent(__VLS_12, new __VLS_12({ ...{}, sign_in: ((true)), }));
__VLS_templateComponents.RegistrationForm;
const __VLS_14 = __VLS_13({ ...{}, sign_in: ((true)), }, ...__VLS_functionalComponentArgsRest(__VLS_13));
const __VLS_15 = __VLS_pickFunctionalComponentCtx(__VLS_12, __VLS_14)!;
}
}
}
}
if (typeof __VLS_styleScopedClasses === 'object' && !Array.isArray(__VLS_styleScopedClasses)) {
__VLS_styleScopedClasses["root"];
__VLS_styleScopedClasses["container"];
}
var __VLS_slots!: {};
return __VLS_slots;
}
