// TODO (CA-5.3): hoy este aviso no muestra nada. Escríbelo tú.
// Con remainingCents mayor que 0 debe decir cuánto falta, por ejemplo
// "Te faltan Q 50.00 para envío gratis". Con 0 debe decir "Tienes envío gratis".
// Usa formatQuetzales y un elemento con role="status" para que el lector de pantalla lo anuncie.
import { formatQuetzales } from '../hooks/useCart';

export interface FreeShippingNoticeProps {
  remainingCents: number;
}

export function FreeShippingNotice({ remainingCents }: FreeShippingNoticeProps) {
  void formatQuetzales;
  void remainingCents;
  return null;
}
