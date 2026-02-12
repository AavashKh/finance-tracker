// src/features/Portfolio/types.ts

export type Prediction = 'Buy' | 'Sell' | 'Hold';

export interface Asset {
    id: string;
    name: string;
    symbol: string;
    quantity: number;
    price: number;
    prediction: Prediction;
    changePercent: number;
    sparklineData: number[]; // data for chart
}