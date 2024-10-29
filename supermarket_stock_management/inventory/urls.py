from django.urls import path
from . import views

urlpatterns = [
    # Existing paths
    path('dashboard', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='product-list'),
    path('products/add/', views.add_product, name='add-product'),
    path('products/edit/<int:pk>/', views.edit_product, name='edit-product'),
    path('products/delete/<int:pk>/', views.delete_product, name='delete-product'),
    path('suppliers/', views.supplier_list, name='supplier-list'),
    path('suppliers/add/', views.add_supplier, name='add-supplier'),
    path('suppliers/edit/<int:pk>/', views.edit_supplier, name='edit-supplier'),
    path('suppliers/delete/<int:pk>/', views.delete_supplier, name='delete-supplier'),
    path('transactions/', views.transaction_list, name='transaction-list'),
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # New paths for password change and cashier management
    path('password-change/', views.change_password, name='change_password'),
    path('cashiers/', views.manage_cashiers, name='manage-cashiers'),
    path('cashiers/add/', views.add_cashier, name='add_cashier'),
    path('cashiers/edit/<int:pk>/', views.edit_cashier, name='edit_cashier'),
    path('cashiers/delete/<int:pk>/', views.delete_cashier, name='delete_cashier'),
    path('add-notification/', views.add_notification, name='add_notification'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('cashier-list/', views.cashier_list, name='cashier_list'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('edit_transaction/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    
    path('transaction-list/', views.transaction_list, name='transaction_list'),
    path('process_sale/', views.process_sale, name='process_sale'),
    path('edit_notification/<int:id>/', views.edit_notification, name='edit_notification'),
    path('notification/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('cashiers/', views.cashier_list, name='cashier_list'),
    path('notifications/', views.notification_list, name='notification_list'),
     path('export/excel/', views.export_excel, name='export_excel'),
    path('export/word/', views.export_word, name='export_word'),
    path('stock-report/', views.stock_report, name='stock_report'),

]
