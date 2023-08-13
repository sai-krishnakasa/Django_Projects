class ApiRouter:
    router_app_labels = {"api"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "api_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "api_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "api_db"
        return None


class AuthRouter:
    router_app_labels = {"auth", "contenttypes", "admin", "sessions"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "users_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "users_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "users_db"
        return None


class AquaRouter:
    router_app_labels = {"aqua"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "aqua_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.router_app_labels:
            return "aqua_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.router_app_labels
            or obj2._meta.app_label in self.router_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == "aqua_db"
        return None
