/**
 * Uses Intl.NumberFormat for locale-aware currency
 * Essential for Internationalization (i18n)
 */

export const formatCurrency = (amount: number, currency = 'USD'): string => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: currency,
    }).format(amount);
}