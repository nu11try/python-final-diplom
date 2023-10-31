from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Contact, ConfirmEmailToken, Shop, Category, Product, Parameter,\
    ProductParameter, Order, OrderItem
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'company', 'position')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'street', 'house', 'phone')
    search_fields = ('user', 'phone')
    ordering = ('user',)
    fields = ('user', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'phone')
    readonly_fields = ('user',)


@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at',)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'shop', 'quantity', 'price', 'price_rrc')
    list_filter = ('shop', 'category')
    fields = (('shop', 'category'), 'name', 'model', 'external_id', 'quantity', ('price', 'price_rrc'))
    readonly_fields = ('category', 'shop')


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ('product', 'parameter', 'value')
    list_filter = ('parameter',)
    readonly_fields = ('product', 'parameter')
    fields = ('product', 'parameter', 'value')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated', 'user', 'status')
    list_display_links = ('created',)
    list_filter = ('status',)
    readonly_fields = ('id', 'user', 'created', 'updated', 'contact')
    fields = ('id', 'user', 'status', 'contact', 'created', 'updated')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product_name', 'category', 'shop', 'quantity')
    list_display_links = ('product_name',)
    list_filter = ('shop', 'category')
    ordering = ('order', 'category', 'shop')
    readonly_fields = ('order_id', 'order', 'category', 'shop', 'product_name', 'external_id')
    fields = (('order_id', 'order'), 'category', 'shop', 'product_name', 'external_id', 'quantity', ('price', 'total_amount'))