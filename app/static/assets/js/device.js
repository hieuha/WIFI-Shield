var ip = {
    busy: false,
    uri: null,
    $dom: null,
    $http: null,
    delay: 60000,
    fetch: function (uri) {
        if (document.hidden) {
            return this.onFinish()
        }
        if (this.busy) {
            return
        }
        var self = this
        var uri = this.uri || uri
        this.onStart(uri)
        this.$http.get(uri, function (data) {
            self.onFinish()
            if (!data.status) {
                return self.onFail(data)
            }
            return self.onSuccess(data)
        }, 'json')
    },
    onFail: function (data) {
        var $msg = $('<div class="alert alert-danger" role="alert"></div>')
        $msg.text(data.message)
        this.$dom.html($msg)
    },
    onSuccess: function (data) {
        var $msg = $('<div class="alert alert-success" role="alert"></div>')
        $msg.text(data.message)
        this.$dom.html($msg)
    },
    onStart: function (uri) {
        this.busy = true
        this.uri = uri
        this.$dom.html('<div class="alert alert-warning" role="alert">Loading...</div>')
    },
    onFinish: function () {
        var self = this
        this.busy = false
        setTimeout(function () {
            self.fetch()
        }, this.delay)
    },
}
jQuery(document).ready(function($) {
    ip.$http = $
    ip.$dom = $('#ip')
    ip.fetch(window.URL_CHECK_INTERNET)
})