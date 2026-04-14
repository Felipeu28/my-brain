declare global {
  type ThemeChangeEvent = CustomEvent<any>;
  type ReaderModeChangeEvent = CustomEvent<any>;
  type NavEvent = CustomEvent<any>;
  type PreNavEvent = CustomEvent<any>;

  interface CustomEventMap {
    themechange: ThemeChangeEvent;
    readermodechange: ReaderModeChangeEvent;
    nav: NavEvent;
    prenav: PreNavEvent;
  }

  type ContentIndex = Record<string, any>;

  var fetchData: Promise<any>;

  interface Window {
    addCleanup: (fn: (...args: any[]) => void) => void;
    spaNavigate: (url: URL, isBack?: boolean) => Promise<void>;
  }

  interface DocumentEventMap extends CustomEventMap {}
}

export {};
