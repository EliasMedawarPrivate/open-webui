import { get } from 'svelte/store';
import {  temporaryChatEnabled } from '$lib/stores';

if (typeof window !== 'undefined') {
  const originalFetch = window.fetch;
  window.fetch = (input, init = {}) => {
    const raw = get(temporaryChatEnabled);
    if (typeof raw === 'boolean') {
      init.headers = {
        ...(init.headers || {}),
        'X-TemporaryChatEnabled': raw.toString()
      };
      return originalFetch(input, init);
    }else{
          return originalFetch(input, init);
    }
    
  };
}