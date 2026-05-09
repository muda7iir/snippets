/** @odoo-module **/

import { SnippetOption } from "@web_editor/js/snippets.options";
import { registry } from "@web/core/registry";

export class NxPropertyShowcaseOptions extends SnippetOption {
    setLayout(previewMode, widgetValue) {
        this.$target.toggleClass("s_nx_property_showcase_3cols", widgetValue === "3");
        this.$target.toggleClass("s_nx_property_showcase_2cols", widgetValue === "2");
    }

    setShowPrice(previewMode, widgetValue) {
        this.$target.toggleClass("s_nx_property_showcase_hide_price", !widgetValue);
    }

    setShowLocation(previewMode, widgetValue) {
        this.$target.toggleClass("s_nx_property_showcase_hide_location", !widgetValue);
    }

    setShowSpecs(previewMode, widgetValue) {
        this.$target.toggleClass("s_nx_property_showcase_hide_specs", !widgetValue);
    }

    setAnimation(previewMode, widgetValue) {
        this.$target.toggleClass("s_nx_property_showcase_animate", widgetValue === "on");
        if (widgetValue === "on" && window.NxScrollReveal) {
            window.NxScrollReveal.observeElements(this.$target[0]);
        }
    }

    setCardStyle(previewMode, widgetValue) {
        this.$target.toggleClass("s_nx_property_showcase_minimal", widgetValue === "minimal");
        this.$target.toggleClass("s_nx_property_showcase_full", widgetValue === "full");
    }
}

registry.category("website_builder_components").add("NxPropertyShowcaseOptions", {
    component: NxPropertyShowcaseOptions,
    selector: ".s_nx_property_showcase",
});
