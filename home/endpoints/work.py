from django.urls import path
from home.views.work import WorkList, WorkDetail, WorkUpdate, WorkCreate, WorkDelete

urlpatterns = [
path('work/', WorkList.as_view(), name='work-list'),
path('work/create/', WorkCreate.as_view(), name='works-create'),    
path('work/<int:pk>', WorkDetail.as_view(), name='works-detail'),
path('work/update/<int:pk>/', WorkUpdate.as_view(), name='works-update'),
path('work/delete/<int:pk>', WorkDelete.as_view(), name='works-delete'),
]
