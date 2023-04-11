from django.shortcuts import redirect


def refresh(atendimento_vinculado):
    print('refresh')
    return redirect('atendimento', pk=atendimento_vinculado)
